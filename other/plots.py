import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_one_box(xyxy, img, color=None, label=None, line_thickness=3):
    """
    Рисует один bounding box на изображении
    
    Параметры:
        xyxy (list или np.array): Координаты bbox в формате [x1, y1, x2, y2]
        img (numpy.ndarray): Изображение в формате OpenCV (BGR)
        color (tuple): Цвет прямоугольника в формате BGR
        label (str): Текст подписи
        line_thickness (int): Толщина линий прямоугольника
    """
    # Определяем цвет (если не задан)
    if color is None:
        color = (0, 255, 0)  # Зеленый по умолчанию
    
    # Преобразуем координаты в целые числа
    x1, y1, x2, y2 = map(int, xyxy)
    
    # Рисуем прямоугольник
    cv2.rectangle(img, (x1, y1), (x2, y2), color, line_thickness)
    
    # Если есть подпись
    if label:
        # Определяем размер текста
        font_scale = 0.6
        font_thickness = 1
        
        # Получаем размеры текста
        (text_width, text_height), _ = cv2.getTextSize(
            label, 
            cv2.FONT_HERSHEY_SIMPLEX, 
            font_scale, 
            font_thickness
        )
        
        # Рисуем подложку для текста
        cv2.rectangle(
            img, 
            (x1, y1 - text_height - 10), 
            (x1 + text_width, y1), 
            color, 
            -1  # Заливка
        )
        
        # Добавляем текст
        cv2.putText(
            img, 
            label, 
            (x1, y1 - 5), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            font_scale, 
            (255, 255, 255),  # Белый текст
            font_thickness, 
            cv2.LINE_AA
        )