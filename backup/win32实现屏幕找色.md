---
Title: win32实现屏幕找色
Date: 2016-03-12
Modified: 2016-03-12
---

实现屏幕找色功能的基本思路是将目标区域内的像素颜色，逐个与目标颜色比对，直到找到为止。

win32中有个函数叫做GetPixel()，这个函数可以用来获取屏幕上某个点的RGB值，用这个函数虽然可以实现我们的目标，但是在目标区域较大的情况下，GetPixel()存在严重的效率问题，找色非！常！慢！

这里有一种效率比较高的屏幕找色函数的实现，主要步骤是：

1. 使用BitBlt函数将屏幕贴图到内存兼容DC中
2. 使用GetBitmapBits函数将bitmap图片的所有颜色值一次性输入到缓冲区中
3. 将缓冲区中的颜色值与目标颜色进行比对

实现代码如下：

```c
// 在rect的矩形区域内查找颜色为rgb的像素点
POINT FindColor(RECT rect, DWORD rgb)
{
    HDC ScreenDC = GetDC(NULL);
    HDC memScreenDC = CreateCompatibleDC(ScreenDC);
    int width = rect.right - rect.left;
    int height = rect.bottom - rect.top;

    HBITMAP hBitmap = CreateCompatibleBitmap(GetDC(NULL), width, height);
    HGDIOBJ hOldbmp = SelectObject(memScreenDC, hBitmap);

    BitBlt(memScreenDC, 0, 0, width, height, ScreenDC, rect.left, rect.top, SRCCOPY);
    SelectObject(memScreenDC, hOldbmp);

    BYTE *bmpBuffer = new BYTE[width*height * 4];
    GetBitmapBits(hBitmap, width*height * 4, bmpBuffer);

    DeleteObject(hBitmap);
    DeleteDC(memScreenDC);

    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            int b = bmpBuffer[row * width * 4 + col * 4];
            int g = bmpBuffer[row * width * 4 + col * 4 + 1];
            int r = bmpBuffer[row * width * 4 + col * 4 + 2];
            if (r == GetRValue(rgb) && g == GetGValue(rgb) && b == GetBValue(rgb))
            {
                delete bmpBuffer;
                return POINT{ col, row };
            }
        }
    }
    delete bmpBuffer;
    return POINT{ -1,-1 };
}
```

这个函数在1366*768的矩形区域中找色一次耗时大约40ms，效率还算可以。如果需要大量使用，则可以修改代码，不要重复的创建和删除资源，比如创建DC和删除DC，分配缓冲区和回收缓冲区。
