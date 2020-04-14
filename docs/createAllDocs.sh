#!/bin/bash
# Script zum erstellen aller Documente
asciidoctor -r asciidoctor-pdf -b pdf ./anforderung/README.adoc -o ./anforderung/anforderungsanalyse.pdf
asciidoctor -r asciidoctor-pdf -b pdf ./anwender/README.adoc -o ./anwender/documentation.pdf
asciidoctor -r asciidoctor-pdf -b pdf ./entwickler/README.adoc -o ./entwickler/documentation_developer.pdf