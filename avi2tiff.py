import cv2
import tifffile as tiff
from PIL import Image
import cv2

def avi_to_single_bigtiff(input_path, output_path):
    # Open the video file
    cap = cv2.VideoCapture(input_path)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Get the video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Create an empty list to hold the frames
    

    tiff_writer=tiff.TiffWriter(output_path, bigtiff=True)
    
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Break the loop if no frame is read
        if not ret:
            break

        tiff_writer.save(frame, compression=0, metadata={}, contiguous=False)

        
    # Release the video capture object
    cap.release()    

    print(f"Conversion complete. The video has been saved as a single BigTIFF file: {output_path}")

if __name__ == "__main__":
    input_video_path = 'inertial_flow.avi'
    output_bigtiff_path = "inertial_flow.tif"

    avi_to_single_bigtiff(input_video_path, output_bigtiff_path)
    """ im=cv2.imread("gerum_screenshot.tif", cv2.IMREAD_UNCHANGED)
    cv2.imshow("wow", im)
    cv2.waitKey(0) """