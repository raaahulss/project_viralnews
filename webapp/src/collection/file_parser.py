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


def get_file(path):
    fp = FileParser()
    word_file = fp.parse(path)
    return word_file


if __name__ == '__main__':
    word_file = get_file('./Test.docx')
    print(word_file.title)
    print(word_file.body)
