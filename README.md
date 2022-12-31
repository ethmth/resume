# Resume

I'm Ethan Thomas, and this is my resume, written in LaTeX.

## Viewing

To view the resume, simply click on the **EthanThomasResume.pdf** file above.

This resume is also pointed to by my personal website, [ethanmt.com/resume](https://www.ethanmt.com/resume). Upon clicking the "View/Download PDF Resume" button on the _Resume_ page, or going directly to [ethanmt.com/resume_pdf](https://www.ethanmt.com/resume_pdf), you should be redirected to a [Google PDF viewer](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/ethmth/resume/main/EthanThomasResume.pdf). The PDF viewer displays the current updated resume present in the **main** branch.

Click [here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/ethmth/resume/main/EthanThomasResume.pdf) to view the resume in the Google PDF Viewer.

## Building

Clone the git repo.

```sh
git clone https://github.com/ethmth/resume.git
cd resume/
```

Ensure `pdflatex` is installed, then run

```sh
pdflatex  -synctex=1 -interaction=nonstopmode -file-line-error -recorder  EthanThomasResume.tex
```

Alternatively, run the provided `build.sh` script.

```sh
chmod +x build.sh
./build.sh
```

The pdf file should be generated in your current directory.
