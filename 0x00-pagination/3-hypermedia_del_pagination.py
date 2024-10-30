from typing import List, Dict, Any
import csv


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10
                        ) -> Dict[str, Any]:
        """Provide page of data and pagination info, resilient to deletions."""
        assert index is not None and 0 <= index < len(self.indexed_dataset()),
        (
            "Index out of range"
        )

        data = []
        current_index = index
        count = 0
        indexed_data = self.indexed_dataset()

        # Collect page_size items, skipping deleted items
        while count < page_size and current_index < len(indexed_data):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                count += 1
            current_index += 1

        # Set next index to current_index if we didn't reach end of dataset
        next_index = current_index if current_index <
        len(indexed_data) else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
