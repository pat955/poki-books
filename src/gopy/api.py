"""
run ./scripts/test.sh for actual testing, it creates and resets the test database

"""
# python wrapper for package github.com/pat955/poki_books/api within overall package api
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy build -output=gopy -vm=python3 ../api

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _api
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from api import api
# and then refer to everything using api. prefix
# packages imported by this package listed below:




# ---- Types ---

# Python type for slice []api.Book
class Slice_api_Book(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_api.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_api.IncRef(self.handle)
		else:
			self.handle = _api.Slice_api_Book_CTor()
			_api.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Iterable):
					raise TypeError('Slice_api_Book.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_api.DecRef(self.handle)
	def __str__(self):
		s = 'api.Slice_api_Book len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'api.Slice_api_Book([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _api.Slice_api_Book_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			if key.step == None or key.step == 1:
				st = key.start
				ed = key.stop
				if st == None:
					st = 0
				if ed == None:
					ed = _api.Slice_api_Book_len(self.handle)
				return Slice_api_Book(handle=_api.Slice_api_Book_subslice(self.handle, st, ed))
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return Book(handle=_api.Slice_api_Book_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_api.Slice_api_Book_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, _collections_abc.Iterable):
			raise TypeError('Slice_api_Book.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = Book(handle=_api.Slice_api_Book_elem(self.handle, self.index))
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_api.Slice_api_Book_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---
def DB_PATH():
	"""
	DB_PATH Gets Go Variable: api.DB_PATH
	
	"""
	return _api.api_DB_PATH()

def Set_DB_PATH(value):
	"""
	Set_DB_PATH Sets Go Variable: api.DB_PATH
	
	"""
	if isinstance(value, go.GoClass):
		_api.api_Set_DB_PATH(value.handle)
	else:
		_api.api_Set_DB_PATH(value)



# ---- Interfaces ---


# ---- Structs ---

# Python type for struct api.NoContentError
class NoContentError(go.GoClass):
	"""NoContentError is a custom error type for missing content errors.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_api.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_api.IncRef(self.handle)
		else:
			self.handle = _api.api_NoContentError_CTor()
			_api.IncRef(self.handle)
			if  0 < len(args):
				self.Message = args[0]
			if "Message" in kwargs:
				self.Message = kwargs["Message"]
	def __del__(self):
		_api.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'api.NoContentError{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'api.NoContentError ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def Message(self):
		return _api.api_NoContentError_Message_Get(self.handle)
	@Message.setter
	def Message(self, value):
		if isinstance(value, go.GoClass):
			_api.api_NoContentError_Message_Set(self.handle, value.handle)
		else:
			_api.api_NoContentError_Message_Set(self.handle, value)
	def Error(self):
		"""Error() str
		
		Implement the Error() method for NoContentError to satisfy the error interface.
		"""
		return _api.api_NoContentError_Error(self.handle)

# Python type for struct api.NoPathError
class NoPathError(go.GoClass):
	"""NoPathError is a custom error type for missing title errors.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_api.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_api.IncRef(self.handle)
		else:
			self.handle = _api.api_NoPathError_CTor()
			_api.IncRef(self.handle)
			if  0 < len(args):
				self.Message = args[0]
			if "Message" in kwargs:
				self.Message = kwargs["Message"]
	def __del__(self):
		_api.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'api.NoPathError{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'api.NoPathError ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def Message(self):
		return _api.api_NoPathError_Message_Get(self.handle)
	@Message.setter
	def Message(self, value):
		if isinstance(value, go.GoClass):
			_api.api_NoPathError_Message_Set(self.handle, value.handle)
		else:
			_api.api_NoPathError_Message_Set(self.handle, value)
	def Error(self):
		"""Error() str
		
		Implement the Error() method for NoPathError to satisfy the error interface.
		"""
		return _api.api_NoPathError_Error(self.handle)

# Python type for struct api.NoTitleError
class NoTitleError(go.GoClass):
	"""NoTitleError is a custom error type for missing title errors.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_api.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_api.IncRef(self.handle)
		else:
			self.handle = _api.api_NoTitleError_CTor()
			_api.IncRef(self.handle)
			if  0 < len(args):
				self.Message = args[0]
			if "Message" in kwargs:
				self.Message = kwargs["Message"]
	def __del__(self):
		_api.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'api.NoTitleError{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'api.NoTitleError ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def Message(self):
		return _api.api_NoTitleError_Message_Get(self.handle)
	@Message.setter
	def Message(self, value):
		if isinstance(value, go.GoClass):
			_api.api_NoTitleError_Message_Set(self.handle, value.handle)
		else:
			_api.api_NoTitleError_Message_Set(self.handle, value)
	def Error(self):
		"""Error() str
		
		Implement the Error() method for NoTitleError to satisfy the error interface.
		"""
		return _api.api_NoTitleError_Error(self.handle)

# Python type for struct api.Book
class Book(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_api.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_api.IncRef(self.handle)
		else:
			self.handle = _api.api_Book_CTor()
			_api.IncRef(self.handle)
			if  0 < len(args):
				self.Path = args[0]
			if "Path" in kwargs:
				self.Path = kwargs["Path"]
			if  1 < len(args):
				self.Title = args[1]
			if "Title" in kwargs:
				self.Title = kwargs["Title"]
			if  2 < len(args):
				self.Content = args[2]
			if "Content" in kwargs:
				self.Content = kwargs["Content"]
			if  3 < len(args):
				self.Extension = args[3]
			if "Extension" in kwargs:
				self.Extension = kwargs["Extension"]
			if  4 < len(args):
				self.Notes = args[4]
			if "Notes" in kwargs:
				self.Notes = kwargs["Notes"]
			if  5 < len(args):
				self.Author = args[5]
			if "Author" in kwargs:
				self.Author = kwargs["Author"]
	def __del__(self):
		_api.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'api.Book{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'api.Book ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def Path(self):
		return _api.api_Book_Path_Get(self.handle)
	@Path.setter
	def Path(self, value):
		if isinstance(value, go.GoClass):
			_api.api_Book_Path_Set(self.handle, value.handle)
		else:
			_api.api_Book_Path_Set(self.handle, value)
	@property
	def Title(self):
		return _api.api_Book_Title_Get(self.handle)
	@Title.setter
	def Title(self, value):
		if isinstance(value, go.GoClass):
			_api.api_Book_Title_Set(self.handle, value.handle)
		else:
			_api.api_Book_Title_Set(self.handle, value)
	@property
	def Content(self):
		return _api.api_Book_Content_Get(self.handle)
	@Content.setter
	def Content(self, value):
		if isinstance(value, go.GoClass):
			_api.api_Book_Content_Set(self.handle, value.handle)
		else:
			_api.api_Book_Content_Set(self.handle, value)
	@property
	def Extension(self):
		return _api.api_Book_Extension_Get(self.handle)
	@Extension.setter
	def Extension(self, value):
		if isinstance(value, go.GoClass):
			_api.api_Book_Extension_Set(self.handle, value.handle)
		else:
			_api.api_Book_Extension_Set(self.handle, value)
	@property
	def Notes(self):
		return _api.api_Book_Notes_Get(self.handle)
	@Notes.setter
	def Notes(self, value):
		if isinstance(value, go.GoClass):
			_api.api_Book_Notes_Set(self.handle, value.handle)
		else:
			_api.api_Book_Notes_Set(self.handle, value)
	@property
	def Author(self):
		return _api.api_Book_Author_Get(self.handle)
	@Author.setter
	def Author(self, value):
		if isinstance(value, go.GoClass):
			_api.api_Book_Author_Set(self.handle, value.handle)
		else:
			_api.api_Book_Author_Set(self.handle, value)


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---
def GetBookByPath(db_path, path):
	"""GetBookByPath(str db_path, str path) object, str
	
	Returns book from db with path as argument
	"""
	return Book(handle=_api.api_GetBookByPath(db_path, path))


# ---- Functions ---
def AddBook(db_path, book):
	"""AddBook(str db_path, object book) str
	
	Connects to db and adds book to database
	"""
	return _api.api_AddBook(db_path, book.handle)
def AddNotesByPath(db_path, notes, path):
	"""AddNotesByPath(str db_path, str notes, str path) str
	
	Add notes using path as identifier
	"""
	return _api.api_AddNotesByPath(db_path, notes, path)
def RemoveBook(db_path, path):
	"""RemoveBook(str db_path, str path) str
	
	Removes book from database
	"""
	return _api.api_RemoveBook(db_path, path)
def ResetNotes(db_path):
	"""ResetNotes(str db_path) str
	
	Empties all notes
	"""
	return _api.api_ResetNotes(db_path)
def GetAllBooks(db_path):
	"""GetAllBooks(str db_path) []object, str"""
	return Slice_api_Book(handle=_api.api_GetAllBooks(db_path))
def GetContentByTitle(db_path, title):
	"""GetContentByTitle(str db_path, str title) str, str
	
	From database gets content with title as argument
	"""
	return _api.api_GetContentByTitle(db_path, title)
def GetNotesByPath(db_path, path):
	"""GetNotesByPath(str db_path, str path) str, str
	
	Get notes with path as the identifier
	"""
	return _api.api_GetNotesByPath(db_path, path)
def ResetTable(dp_path):
	"""ResetTable(str dp_path) str
	
	Removes all rows from table
	"""
	return _api.api_ResetTable(dp_path)


