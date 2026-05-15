import cv2
import pygame
import sys
import subprocess
import os

def extract_audio(video_path):
    audio_path = os.path.splitext(video_path)[0] + '.wav'
    subprocess.run([
        'ffmpeg', '-i', video_path,
        '-q:a', '0', '-map', 'a',
        audio_path, '-y'
    ], capture_output=True)
    return audio_path

# Init pygame
pygame.init()
screen = pygame.display.set_mode((500, 400), pygame.NOFRAME)
pygame.display.set_caption('')

# Position window top left
import ctypes
hwnd = pygame.display.get_wm_info()['window']
ctypes.windll.user32.SetWindowPos(hwnd, 0, 0, 0, 500, 400, 0)

video_path = sys.argv[1] if len(sys.argv) > 1 else 'dog.mp4'

# Extract and play audio
audio_path = extract_audio(video_path)
pygame.mixer.init()
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play(-1)  # -1 loops forever

# Load video
cap = cv2.VideoCapture(video_path)
clock = pygame.time.Clock()
fps = cap.get(cv2.CAP_PROP_FPS)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        pygame.mixer.music.rewind()
        continue

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.transpose(frame)
    surface = pygame.surfarray.make_surface(frame)
    surface = pygame.transform.scale(surface, (500, 400))
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    clock.tick(fps)

cap.release()
pygame.quit()