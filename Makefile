# Set flags for the different operator systems
# =============================================================================
# Linux
DELCALL = rm -f
# PROCDIR = /usr/local/texlive/2016/bin/x86_64-linux
ARGP = -shell-escape
# =============================================================================

# Flags and arguments
# =============================================================================
PROC = pdflatex
PROCARG = -interaction=nonstopmode
# =============================================================================

# Files to be cleaned
# =============================================================================
WASTE = .aux .bbl .blg .log .out .tex.latexmain .toc
# =============================================================================

# Find the TARGET
# =============================================================================
TEXTARGET = $(wildcard *.tex)
TARGET = $(TEXTARGET:.tex=)
# =============================================================================

# Set other dependency macros
# =============================================================================
# http://stackoverflow.com/questions/14289513/makefile-rule-that-depends-on-all-files-under-a-directory-including-within-subd
# http://stackoverflow.com/questions/2621513/how-to-use-find-command-to-find-all-files-with-extensions-from-list
FIGURES = $(shell find fig -regex ".*\.\(jpeg\|jpg\|png\|svg\|pdf\)")
# =============================================================================

# Make
# =============================================================================
$(TARGET).pdf: $(TARGET).bbl
	$(info ->   making $(TARGET).pdf)
	$(PROC) $(TEXTARGET)
	$(PROC) $(TEXTARGET)

$(TARGET).bbl : $(TARGET).aux
	$(info ->   making $(TARGET).bbl)
	bibtex $(TARGET).aux

$(TARGET).aux : $(TEXTARGET) $(FIGURES)
	$(info ->   making $(TARGET).aux)
	$(PROC) $(PROCARG) $(TEXTARGET)
# =============================================================================

# Clean
# =============================================================================
# Make a phony rule
.PHONY: clean

clean:
	$(DELCALL) $(foreach SUFFIX,$(WASTE),$(TARGET)$(SUFFIX))
# =============================================================================
