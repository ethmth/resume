#latexmk -pdf -xelatex -quiet resume.tex
#latexmk -pdf resume.tex
pdflatex  -synctex=1 -interaction=nonstopmode -file-line-error -recorder  resume.tex