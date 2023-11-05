from rapidx.app.data.db.db import Db
from rapidx.app.data.importer import Importer
from rapidx.app.data.filecache import FileCache
from rapidx.app.data.multifileset.multifilesetregistrationhelper import MultiFileSetRegistrationHelper
from rapidx.app.data.multifileset.dicommultifilesetfactory import DicomMultiFileSetFactory
from rapidx.app.utils import create_random_name


class DicomMultiFileSetImporter(Importer):
    def __init__(self, path: str) -> None:
        name = create_random_name('multifileset')
        super(DicomMultiFileSetImporter, self).__init__(name=name, path=path)

    def run(self):    
        with Db() as db:
            helper = MultiFileSetRegistrationHelper(name=self.name(), path=self.path(), db=db)
            multiFileSetModel = helper.execute()
            self.setData(multiFileSetModel)
            factory = DicomMultiFileSetFactory()
            factory.signal().progress.connect(self._updateProgress)
            factory.signal().finished.connect(self._importFinished)
            dicomMultiFileSet = factory.create(multiFileSetModel=multiFileSetModel, db=db)
            cache = FileCache()
            for dicomFileSet in dicomMultiFileSet:
                for dicomFile in dicomFileSet:
                    cache.add(file=dicomFile)

    def _updateProgress(self, progress) -> None:
        self.signal().progress.emit(progress)

    def _importFinished(self, value) -> None:
        self.signal().finished.emit(value)