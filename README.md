# my_text_extracter
Today, I successfully solved the text-extracting problem I had for 3 days after searching the internet for a solution and could not get a better one.

I just wanted to extract text from images! So why not code my own script!

Almost all the available online converters require a premium subscription in order to use their 0-C-R Technology.. The few ones I found could not do exactly what I wanted!

So I had about 20 pages of these pdf-image format documents that were scanned by a certain cam scanner and sent over! My challenge was to convert them to text since the original document could have been misplaced.

I decided to write my own script to solve the issue at hand! I mainly used two important libraries every Pythonista should know 🙇‍♂️.
🔸Pytesseract
🔸OpenCV

✨ Pytesseract
Pytesseract is a wrapper for Google's Tesseract-OCR Engine. It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries, including jpeg, png, gif, bmp, tiff, and othersimage.pngTesseract is an excellent open-source engine for OCR. But it can't read PDFs on its own. So I had to convert my pdfs to png formats.

✨ OCV
OpenCV-Python is a library of Python bindings designed to solve computer vision problems OpenCV-Python makes use of Numpy, which is a highly optimized library for numerical operations with a MATLAB-style syntax. All the OpenCV array structures are converted to and from Numpy arrays.


This also makes it easier to integrate with other libraries that use Numpy such as SciPy and Matplotlib. I also used os built-in module for walking and navigating through my machine.
