#PNG overlay (replacement for cvzone.overlayPNG)
def overlayPNG(background, overlay, x, y):
    h, w, _ = overlay.shape

    if y + h > background.shape[0] or x + w > background.shape[1]:
        return background  # prevent crash

    alpha = overlay[:, :, 3] / 255.0

    for c in range(3):
        background[y:y+h, x:x+w, c] = (
            alpha * overlay[:, :, c] +
            (1 - alpha) * background[y:y+h, x:x+w, c]
        )

    return background
