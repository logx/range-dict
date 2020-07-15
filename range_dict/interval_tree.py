from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import date, datetime
from typing import TypeVar, Optional, Tuple, Any

logger = logging.getLogger("range_dict.interval_tree")

T = TypeVar('T', int, float, date, datetime)


@dataclass
class Node:
    range_key: Tuple[T, T]

    max_key: T

    value: Any

    left: Optional[Node] = None
    right: Optional[Node] = None


class IntervalTree:
    root: Optional[Node] = None

    def insert(self, range_key: Tuple[T, T], value: Any) -> None:
        lower_key, higher_key = range_key

        if lower_key > higher_key:
            range_key = higher_key, lower_key
            logger.warning(f"Inverting order of keys passed to Range Dict's Interval Tree -> {range_key}")

        if not self.root:
            self.root = Node(range_key, range_key[1], value)
            return

        self._insert(self.root, range_key, value)

    def _insert(self, node: Node, range_key: Tuple[T, T], value: Any):
        """
        Utility function, hare actual recursive inserting happens.
        """
        lower_key, higher_key = range_key
        node_lower_key, node_higher_key = node.range_key

        if lower_key < node_lower_key:
            if not node.left:
                node.left = Node(range_key, range_key[1], value)
            else:
                self._insert(node.left, range_key, value)
        else:
            if not node.right:
                node.right = Node(range_key, range_key[1], value)
            else:
                self._insert(node.right, range_key, value)

        if node.max_key < higher_key:
            node.max_key = higher_key
