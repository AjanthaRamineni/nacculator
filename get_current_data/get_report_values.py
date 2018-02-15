import os
import sys
from resizeimage import resizeimage
from fpdf import FPDF

final_result = {}

def create_folder(out_dir):
    #Check if directory exists. If not, create it.
    if not os.path.exists(out_dir):
        try:
            os.makedirs(out_dir)
            print "Created Folder"
        except Exception as e:
            raise e

def get_values():
    from wand.image import Image

    # Converting first page into JPG
    print "Entered Values"
    current_directory = os.getcwd()
    image_folder = os.path.join(current_directory, "Images")
    if not os.path.exists(image_folder):
        create_folder(image_folder)

    image_save = os.path.join(image_folder,"first.png")
    with Image(filename="broker93_20180215.pdf[0]") as img:
         img.save(filename=image_save)

    from PIL import Image
    img = Image.open(image_save)
    img = img.convert('L')
    print "Extracting Images"
    # Getting ADC
    adc_img = os.path.join(image_folder,"total_adc.png")
    img1 = img.crop((155.59, 167.6, 224.35, 192.24))
    # img1 = resizeimage.resize_contain(img1, [800, 800])
    img1.save(adc_img)
    pdf = FPDF()
    pdf.add_page()
    pdf.image(adc_img)
    pdf.output("yourfile.pdf", "F")
    
    auto_img = os.path.join(image_folder,"auto.png")
    img2 = img.crop((160.128, 190.44, 228.88, 205.776))
    # img2 = resizeimage.resize_contain(img1, [100, 100])
    img2.save(auto_img)

    npform = os.path.join(image_folder,"np.png")
    img2 = img.crop((148.176,201.528,186.841,217.512))
    img2.save(npform)

    finalized6 = os.path.join(image_folder,"finalized6.png")
    img2 = img.crop((409.104, 118.656, 527.112, 129.096))
    img2.save(finalized6)

    date = os.path.join(image_folder,"date.png")
    img1 = img.crop((516.816, 38.88, 594.288, 60.408))
    img1.save(date)

    # get data
    import pyocr
    import pyocr.builders
    # from PIL import Image
    tools = pyocr.get_available_tools()[0]
    text = tools.image_to_string(Image.open(date),
                                 builder=pyocr.builders.DigitBuilder())

    print text


def main():
    # input_file = argc
    print "Hello"
    get_values()

if __name__ == '__main__':
    main()
