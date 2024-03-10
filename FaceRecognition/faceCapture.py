import os
import cv2

def capture_images(num_images):
    camera = cv2.VideoCapture(0)  # Use the default camera (0)

    # Create the "faces" directory if it doesn't exist
    if not os.path.exists("faces"):
        os.makedirs("faces")

    for i in range(num_images):
        return_value, image = camera.read()
        cv2.imwrite(f"faces/person{i+1}.jpg", image)  # Save the captured image in "faces" directory
        print(f"Image {i+1} captured!")

    camera.release()  # Release the camera
    cv2.destroyAllWindows()  # Close the window

if __name__ == "__main__":
    num_images = 5  # Number of images to capture
    capture_images(num_images)
