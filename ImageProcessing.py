import cv2

class ImageProcessing:
    @staticmethod
    def apply_clahe(frame_img, for_value, clip_limit, tile_grid_size):
        """Apply CLAHE processing to the given frame."""
        lab_img = cv2.cvtColor(frame_img, cv2.COLOR_BGR2LAB)
        l_channel, a_channel, b_channel = cv2.split(lab_img)

        for _ in range(int(for_value)):
            clahe = cv2.createCLAHE(clipLimit=float(clip_limit), tileGridSize=(int(tile_grid_size), int(tile_grid_size)))
            l_channel = clahe.apply(l_channel)

        lab_img = cv2.merge((l_channel, a_channel, b_channel))
        median_lab_img = cv2.medianBlur(lab_img, 3)
        return cv2.cvtColor(median_lab_img, cv2.COLOR_LAB2BGR)
