# Name: Alex Wong
# Student number: A01189960
import concurrent.futures
import pprint
import threading
import time

from city_processor import CityDatabase, ISSDataRequest, CityOverheadTimes, City


class CityOverheadTimeQueue:

    def __init__(self):
        self.__data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: CityOverheadTimes) -> None:
        self.__data_queue.append(overhead_time)

    def get(self) -> CityOverheadTimes:
        """
        method is responsible to removing an element from a Queue
        FIFO first item first out
        """
        first_item_first_out = self.__data_queue[0]
        del self.__data_queue[0]
        return first_item_first_out

    def __len__(self) -> int:
        """
        returns the length of the data queue
        """
        return len(self.__data_queue)


class ProducerThread(threading.Thread):

    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        """
        This method initializes the class with a list of City Objects as well as a CityOverheadTimeQueue
        """
        super().__init__()
        self.cities = cities
        self.queue = queue

    def run(self) -> None:
        """
        It then proceeds to add the city to the queue. After reading in 5 cities, the thread should sleep for 1 second.
        """
        with self.queue.access_queue_lock:
            city_count = 0
            for city in self.cities:
                self.queue.put(ISSDataRequest.get_overhead_pass(city))
                city_count += 1
                if city_count % 5 == 0:
                    time.sleep(1)


class ConsumerThread(threading.Thread):
    """
    Consumes the producer
    """

    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self.queue = queue
        self.data_incoming = True

    def run(self) -> None:
        with self.queue.access_queue_lock:
            while self.data_incoming or self.queue.__len__() > 0:
                print(self.queue.get())
                time.sleep(0.5)
                if self.queue.__len__() == 0:
                    print("is sleeping since queue is empty")
                    self.data_incoming = False
                    time.sleep(0.75)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def main():
    file = "city_locations_test.xlsx"
    start = time.time()
    queue = CityOverheadTimeQueue()
    database = CityDatabase(file)
    item_list = len(database.city_db)
    producer_threads = 3
    amount_thread = round(item_list / producer_threads)

    producer_one = ProducerThread(database.city_db[0:amount_thread:], queue)
    producer_two = ProducerThread(database.city_db[amount_thread:(
            producer_threads*2):], queue)
    producer_three = ProducerThread(database.city_db[(producer_threads*2)::], queue)
    consumer_one = ConsumerThread(queue)

    producer_one.run()
    producer_two.run()
    producer_three.run()

    consumer_one.run()

    print(f"Total duration: {time.time() - start} seconds")


if __name__ == '__main__':
    main()
