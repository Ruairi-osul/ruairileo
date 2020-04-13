import numpy as np

# you can load in the functions from the freeze analysis package here, or write them in the class


class FreezeProcessor:
    @staticmethod
    def some_eztrack_function(eztrack_arg1, etc):
        """
        You might want to include the eztrack functions in the class.
        @staticmethod just means that the object it not referenced in the method call.
        For our case it means you can use the functions the same way as normal functions.
        To access these functions elsewhere in the class, call self.some_eztrack_function(eztrack_arg1="some_value").
        """
        # copy and paste here!
        pass  # pass just means ignore this

    def process_data(self, path: str) -> np.ndarray:
        """
        Your job is to write this method.

        Takes a path of a video file and returns a numpy array of freezing times.
        """
        # your code here
        pass


if __name__ == "__main__":
    # write code here to test your class is doing what you expect
    # for example to test the process_data method

    VIDEO_PATH = "videos/my_video.avi"
    processor = FreezeProcessor()
    events = processor.process_data(VIDEO_PATH)
    print(events)
