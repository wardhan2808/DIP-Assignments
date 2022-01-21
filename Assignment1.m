Img = imread('Yashwardhan.jpg');
dim = size(Img);

blue = Img(:,:,1);
green = Img(:,:,2);
red = Img(:,:,3);
gray = uint8((red/3)+(green/3)+(blue/3));

for i = 1:dim(1)
    for j = 1:dim(2)
        if gray(i,j) > 180
            bin(i,j) = 1;
        else
            bin(i,j) = 0;
        end
        I1(i,j) = uint8(gray(i,j) + bin(i,j));
        I2(i,j) = uint8(gray(i,j) + 20);
    end
end

subplot(2,4,1), imshow(Img), title('Original Image')
subplot(2,4,2), imshow(red), title('Red Layer')
subplot(2,4,3), imshow(green), title('Green Layer')
subplot(2,4,4), imshow(blue), title('Blue Layer')
subplot(2,4,5), imshow(gray), title('Gray Scale Image')
subplot(2,4,6), imshow(bin), title('Binary Image')
subplot(2,4,7), imshow(I1), title('Addition of gray and binary images')
subplot(2,4,8), imshow(I2), title('20 added to gray image')