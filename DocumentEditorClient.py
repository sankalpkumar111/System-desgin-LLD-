from abc import ABC, abstractmethod

# Base abstract class
class DocumentElement(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class TextElement(DocumentElement):
    def __init__(self, text: str):
        self.__text = text

    def render(self) -> str:
        return self.__text

class ImageElement(DocumentElement):
    def __init__(self, path: str):
        self.__path = path

    def render(self) -> str:
        # Fixed variable name here from _image_path to __path
        return f"[Image: {self.__path}]"

class NewLineElement(DocumentElement):
    def render(self) -> str:
        return "\n"

class TabSpaceElement(DocumentElement):
    def render(self) -> str:
        return "\t"

class Document:
    def __init__(self):
        self._document_elements = []

    def add_element(self, element: DocumentElement):
        self._document_elements.append(element)

    def render(self) -> str:
        result = ""
        for element in self._document_elements:
            result += element.render()
        return result

class Persistence(ABC):
    @abstractmethod
    def save(self, data: str):
        pass

class FileStorage(Persistence):
    def save(self, data: str):
        try:
            with open("document.txt", "w") as out_file:
                out_file.write(data)
            print("Document saved to document.txt")
        except IOError:
            print("Error: Unable to open file for writing.")

class DBStorage(Persistence):
    def save(self, data: str):
        print(f"Saving data to database: {data}")

class DocumentEditor:
    def __init__(self, document: Document, storage: Persistence):
        self._document = document
        self._storage = storage
        self._rendered_document = ""

    def add_text(self, text: str):
        self._document.add_element(TextElement(text))

    def add_image(self, image_path: str):
        self._document.add_element(ImageElement(image_path))

    def add_new_line(self):
        self._document.add_element(NewLineElement())

    def add_tab_space(self):
        self._document.add_element(TabSpaceElement())

    def render_document(self) -> str:
        if not self._rendered_document:
            self._rendered_document = self._document.render()
        return self._rendered_document

    def save_document(self):
        self._storage.save(self.render_document())


# Example usage:
if __name__ == "__main__":
    doc = Document()
    storage = FileStorage()
    editor = DocumentEditor(doc, storage)

    editor.add_text("Hello,")
    editor.add_tab_space()
    editor.add_text("World!")
    editor.add_new_line()
    editor.add_image("cat.png")

    print(editor.render_document())
    editor.save_document()
