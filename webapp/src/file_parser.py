import docx


class FileParser(object):
    """
    Interact with file objects
    """
    @staticmethod
    def parse(file_path):
        """
        Parse a file to extract its title and body
        :param file_path: path of a file
        :return: title and body of the file
        """
        doc = docx.Document(file_path)
        word_file = WordFile()
        for paragraph in doc.paragraphs:
            if paragraph.style.name == 'Title':
                word_file.title = paragraph.text
            else:
                word_file.body.append(paragraph.text)
        return word_file


class WordFile(object):
    """
    Word document file object
    """
    def __init__(self):
        self.title = ''
        self.body = []


if __name__ == '__main__':
    fp = FileParser()
    file = fp.parse('./Test.docx')
    print(file.title)
    print(file.body)
