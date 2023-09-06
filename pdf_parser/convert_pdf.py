from PyPDF2 import PdfReader


import os


def main():
    in_dir = 'pdf_dir/'
    out_dir = 'txt_dir/'
    infiles = [p for p in os.listdir(in_dir) if p.endswith('.pdf')]
    for infile in infiles:
        reader = PdfReader(os.path.join(in_dir, infile))
        number_of_pages = len(reader.pages)
        page = reader.pages
        all_text = []
        for page in reader.pages:
            all_text.append(page.extract_text())
        text = '\n'.join(all_text)
        with open(os.path.join(out_dir, infile.split('.')[0]+'.txt'), 'w') as outf:
            outf.write(text)


if __name__ == '__main__':
    main()
