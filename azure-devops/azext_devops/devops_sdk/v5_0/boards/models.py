# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BoardColumnBase(Model):
    """BoardColumnBase.

    :param description: Board column description.
    :type description: str
    :param name: Name of the column.
    :type name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(BoardColumnBase, self).__init__()
        self.description = description
        self.name = name


class BoardColumnCollectionResponse(Model):
    """BoardColumnCollectionResponse.

    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.boards.models.ReferenceLinks>`
    :param board_columns: The resulting collection of BoardColumn.
    :type board_columns: list of :class:`BoardColumn <azure.devops.v5_0.boards.models.BoardColumn>`
    :param eTag: The last change date and time for all the columns in the collection.
    :type eTag: list of str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'board_columns': {'key': 'boardColumns', 'type': '[BoardColumn]'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, _links=None, board_columns=None, eTag=None):
        super(BoardColumnCollectionResponse, self).__init__()
        self._links = _links
        self.board_columns = board_columns
        self.eTag = eTag


class BoardColumnCreate(BoardColumnBase):
    """BoardColumnCreate.

    :param description: Board column description.
    :type description: str
    :param name: Name of the column.
    :type name: str
    :param next_column_id: Next column identifier or supported directive: $first or $last.
    :type next_column_id: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'next_column_id': {'key': 'nextColumnId', 'type': 'str'}
    }

    def __init__(self, description=None, name=None, next_column_id=None):
        super(BoardColumnCreate, self).__init__(description=description, name=name)
        self.next_column_id = next_column_id


class BoardColumnResponse(Model):
    """BoardColumnResponse.

    :param board_column: The resulting BoardColumn.
    :type board_column: :class:`BoardColumn <azure.devops.v5_0.boards.models.BoardColumn>`
    :param eTag: The last change date and time for all the columns in the collection.
    :type eTag: list of str
    """

    _attribute_map = {
        'board_column': {'key': 'boardColumn', 'type': 'BoardColumn'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, board_column=None, eTag=None):
        super(BoardColumnResponse, self).__init__()
        self.board_column = board_column
        self.eTag = eTag


class BoardColumnUpdate(BoardColumnCreate):
    """BoardColumnUpdate.

    :param description: Board column description.
    :type description: str
    :param next_column_id: Next column identifier or supported directive: $first or $last.
    :type next_column_id: str
    :param name: Name of the column.
    :type name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'next_column_id': {'key': 'nextColumnId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, next_column_id=None, name=None):
        super(BoardColumnUpdate, self).__init__(description=description, next_column_id=next_column_id)
        self.name = name


class BoardItemCollectionResponse(Model):
    """BoardItemCollectionResponse.

    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.boards.models.ReferenceLinks>`
    :param board_items: The resulting collection of BoardItem.
    :type board_items: list of :class:`BoardItem <azure.devops.v5_0.boards.models.BoardItem>`
    :param eTag: The last change date and time for all items in the collection.
    :type eTag: list of str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'board_items': {'key': 'boardItems', 'type': '[BoardItem]'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, _links=None, board_items=None, eTag=None):
        super(BoardItemCollectionResponse, self).__init__()
        self._links = _links
        self.board_items = board_items
        self.eTag = eTag


class BoardItemIdAndType(Model):
    """BoardItemIdAndType.

    :param item_id: Item id.
    :type item_id: str
    :param item_type: Item type.
    :type item_type: str
    """

    _attribute_map = {
        'item_id': {'key': 'itemId', 'type': 'str'},
        'item_type': {'key': 'itemType', 'type': 'str'}
    }

    def __init__(self, item_id=None, item_type=None):
        super(BoardItemIdAndType, self).__init__()
        self.item_id = item_id
        self.item_type = item_type


class BoardItemReference(BoardItemIdAndType):
    """BoardItemReference.

    :param item_id: Item id.
    :type item_id: str
    :param item_type: Item type.
    :type item_type: str
    :param unique_id: Board's unique identifier. Compound identifier generated using the item identifier and item type.
    :type unique_id: str
    :param url: Full http link to the resource.
    :type url: str
    """

    _attribute_map = {
        'item_id': {'key': 'itemId', 'type': 'str'},
        'item_type': {'key': 'itemType', 'type': 'str'},
        'unique_id': {'key': 'uniqueId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, item_id=None, item_type=None, unique_id=None, url=None):
        super(BoardItemReference, self).__init__(item_id=item_id, item_type=item_type)
        self.unique_id = unique_id
        self.url = url


class BoardItemResponse(Model):
    """BoardItemResponse.

    :param eTag: The last changed date for the board item.
    :type eTag: list of str
    :param item: The resulting BoardItem.
    :type item: :class:`BoardItem <azure.devops.v5_0.boards.models.BoardItem>`
    """

    _attribute_map = {
        'eTag': {'key': 'eTag', 'type': '[str]'},
        'item': {'key': 'item', 'type': 'BoardItem'}
    }

    def __init__(self, eTag=None, item=None):
        super(BoardItemResponse, self).__init__()
        self.eTag = eTag
        self.item = item


class BoardResponse(Model):
    """BoardResponse.

    :param board: The resulting Board.
    :type board: :class:`Board <azure.devops.v5_0.boards.models.Board>`
    :param eTag: The last date and time the board was changed.
    :type eTag: list of str
    """

    _attribute_map = {
        'board': {'key': 'board', 'type': 'Board'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, board=None, eTag=None):
        super(BoardResponse, self).__init__()
        self.board = board
        self.eTag = eTag


class BoardRowBase(Model):
    """BoardRowBase.

    :param name: Row name.
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(BoardRowBase, self).__init__()
        self.name = name


class BoardRowCollectionResponse(Model):
    """BoardRowCollectionResponse.

    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.boards.models.ReferenceLinks>`
    :param board_rows: The resulting collection of BoardRow.
    :type board_rows: list of :class:`BoardRow <azure.devops.v5_0.boards.models.BoardRow>`
    :param eTag: The last change date and time for all the rows in the collection.
    :type eTag: list of str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'board_rows': {'key': 'boardRows', 'type': '[BoardRow]'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, _links=None, board_rows=None, eTag=None):
        super(BoardRowCollectionResponse, self).__init__()
        self._links = _links
        self.board_rows = board_rows
        self.eTag = eTag


class BoardRowCreate(BoardRowBase):
    """BoardRowCreate.

    :param name: Row name.
    :type name: str
    :param next_row_id: Next row identifier or supported directive: $first or $last.
    :type next_row_id: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'next_row_id': {'key': 'nextRowId', 'type': 'str'}
    }

    def __init__(self, name=None, next_row_id=None):
        super(BoardRowCreate, self).__init__(name=name)
        self.next_row_id = next_row_id


class BoardRowResponse(Model):
    """BoardRowResponse.

    :param board_row: The resulting collection of BoardRow.
    :type board_row: :class:`BoardRow <azure.devops.v5_0.boards.models.BoardRow>`
    :param eTag: The last change date and time for all the rows in the collection.
    :type eTag: list of str
    """

    _attribute_map = {
        'board_row': {'key': 'boardRow', 'type': 'BoardRow'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, board_row=None, eTag=None):
        super(BoardRowResponse, self).__init__()
        self.board_row = board_row
        self.eTag = eTag


class BoardRowUpdate(BoardRowCreate):
    """BoardRowUpdate.

    :param name: Row name.
    :type name: str
    :param next_row_id: Next row identifier or supported directive: $first or $last.
    :type next_row_id: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'next_row_id': {'key': 'nextRowId', 'type': 'str'},
    }

    def __init__(self, name=None, next_row_id=None):
        super(BoardRowUpdate, self).__init__(name=name, next_row_id=next_row_id)


class CreateBoard(Model):
    """CreateBoard.

    :param description: Description of the board.
    :type description: str
    :param name: Name of the board to create.
    :type name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(CreateBoard, self).__init__()
        self.description = description
        self.name = name


class EntityReference(Model):
    """EntityReference.

    :param name: Name of the resource.
    :type name: str
    :param url: Full http link to the resource.
    :type url: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, url=None):
        super(EntityReference, self).__init__()
        self.name = name
        self.url = url


class NewBoardItem(BoardItemIdAndType):
    """NewBoardItem.

    :param item_id: Item id.
    :type item_id: str
    :param item_type: Item type.
    :type item_type: str
    :param column_id: Board column identifier.
    :type column_id: str
    :param next_item_unique_id: Next item unique identifier or supported directive: $first or $last.
    :type next_item_unique_id: str
    :param row_id: Board row identifier.
    :type row_id: str
    """

    _attribute_map = {
        'item_id': {'key': 'itemId', 'type': 'str'},
        'item_type': {'key': 'itemType', 'type': 'str'},
        'column_id': {'key': 'columnId', 'type': 'str'},
        'next_item_unique_id': {'key': 'nextItemUniqueId', 'type': 'str'},
        'row_id': {'key': 'rowId', 'type': 'str'}
    }

    def __init__(self, item_id=None, item_type=None, column_id=None, next_item_unique_id=None, row_id=None):
        super(NewBoardItem, self).__init__(item_id=item_id, item_type=item_type)
        self.column_id = column_id
        self.next_item_unique_id = next_item_unique_id
        self.row_id = row_id


class ReferenceLinks(Model):
    """ReferenceLinks.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class UpdateBoard(Model):
    """UpdateBoard.

    :param description: New description of the board.
    :type description: str
    :param name: New name of the board.
    :type name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(UpdateBoard, self).__init__()
        self.description = description
        self.name = name


class UpdateBoardItem(Model):
    """UpdateBoardItem.

    :param column_id: Board column identifier.
    :type column_id: str
    :param next_item_unique_id: Next unique item identifier or supported directive: $first or $last.
    :type next_item_unique_id: str
    :param row_id: Board row identifier.
    :type row_id: str
    """

    _attribute_map = {
        'column_id': {'key': 'columnId', 'type': 'str'},
        'next_item_unique_id': {'key': 'nextItemUniqueId', 'type': 'str'},
        'row_id': {'key': 'rowId', 'type': 'str'}
    }

    def __init__(self, column_id=None, next_item_unique_id=None, row_id=None):
        super(UpdateBoardItem, self).__init__()
        self.column_id = column_id
        self.next_item_unique_id = next_item_unique_id
        self.row_id = row_id


class BoardColumn(BoardColumnBase):
    """BoardColumn.

    :param description: Board column description.
    :type description: str
    :param name: Name of the column.
    :type name: str
    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.boards.models.ReferenceLinks>`
    :param id: Id of the resource.
    :type id: str
    :param next_column_id: Next column identifier.
    :type next_column_id: str
    :param url: Full http link to the resource.
    :type url: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'str'},
        'next_column_id': {'key': 'nextColumnId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, description=None, name=None, _links=None, id=None, next_column_id=None, url=None):
        super(BoardColumn, self).__init__(description=description, name=name)
        self._links = _links
        self.id = id
        self.next_column_id = next_column_id
        self.url = url


class BoardItem(BoardItemReference):
    """BoardItem.

    :param item_id: Item id.
    :type item_id: str
    :param item_type: Item type.
    :type item_type: str
    :param unique_id: Board's unique identifier. Compound identifier generated using the item identifier and item type.
    :type unique_id: str
    :param url: Full http link to the resource.
    :type url: str
    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.boards.models.ReferenceLinks>`
    :param board_id: Board id for this item.
    :type board_id: int
    :param column: Board column id for this item.
    :type column: str
    :param next_item_unique_id: Next item unique identifier.
    :type next_item_unique_id: str
    :param row: Board row id for this item.
    :type row: str
    """

    _attribute_map = {
        'item_id': {'key': 'itemId', 'type': 'str'},
        'item_type': {'key': 'itemType', 'type': 'str'},
        'unique_id': {'key': 'uniqueId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'board_id': {'key': 'boardId', 'type': 'int'},
        'column': {'key': 'column', 'type': 'str'},
        'next_item_unique_id': {'key': 'nextItemUniqueId', 'type': 'str'},
        'row': {'key': 'row', 'type': 'str'}
    }

    def __init__(self, item_id=None, item_type=None, unique_id=None, url=None, _links=None, board_id=None, column=None, next_item_unique_id=None, row=None):
        super(BoardItem, self).__init__(item_id=item_id, item_type=item_type, unique_id=unique_id, url=url)
        self._links = _links
        self.board_id = board_id
        self.column = column
        self.next_item_unique_id = next_item_unique_id
        self.row = row


class BoardReference(EntityReference):
    """BoardReference.

    :param name: Name of the resource.
    :type name: str
    :param url: Full http link to the resource.
    :type url: str
    :param id: Id of the resource.
    :type id: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, name=None, url=None, id=None):
        super(BoardReference, self).__init__(name=name, url=url)
        self.id = id


class BoardRow(BoardRowBase):
    """BoardRow.

    :param name: Row name.
    :type name: str
    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.boards.models.ReferenceLinks>`
    :param id: Id of the resource.
    :type id: str
    :param next_row_id: Next row identifier.
    :type next_row_id: str
    :param url: Full http link to the resource.
    :type url: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'str'},
        'next_row_id': {'key': 'nextRowId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, _links=None, id=None, next_row_id=None, url=None):
        super(BoardRow, self).__init__(name=name)
        self._links = _links
        self.id = id
        self.next_row_id = next_row_id
        self.url = url


class Board(BoardReference):
    """Board.

    :param name: Name of the resource.
    :type name: str
    :param url: Full http link to the resource.
    :type url: str
    :param id: Id of the resource.
    :type id: int
    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.boards.models.ReferenceLinks>`
    :param description: Description of the board.
    :type description: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'}
    }

    def __init__(self, name=None, url=None, id=None, _links=None, description=None):
        super(Board, self).__init__(name=name, url=url, id=id)
        self._links = _links
        self.description = description


__all__ = [
    'BoardColumnBase',
    'BoardColumnCollectionResponse',
    'BoardColumnCreate',
    'BoardColumnResponse',
    'BoardColumnUpdate',
    'BoardItemCollectionResponse',
    'BoardItemIdAndType',
    'BoardItemReference',
    'BoardItemResponse',
    'BoardResponse',
    'BoardRowBase',
    'BoardRowCollectionResponse',
    'BoardRowCreate',
    'BoardRowResponse',
    'BoardRowUpdate',
    'CreateBoard',
    'EntityReference',
    'NewBoardItem',
    'ReferenceLinks',
    'UpdateBoard',
    'UpdateBoardItem',
    'BoardColumn',
    'BoardItem',
    'BoardReference',
    'BoardRow',
    'Board',
]
