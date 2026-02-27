import React from 'react';
import { PhotoProvider, PhotoView } from 'react-photo-view';
import 'react-photo-view/dist/react-photo-view.css';

interface ImageViewProps extends React.ImgHTMLAttributes<HTMLImageElement> {}

export const ImageView: React.FC<ImageViewProps> = ({ src, children, ...rest }) => {
  if (!src) return null;

  return (
    <PhotoProvider>
      <PhotoView src={src}>
        <img
          src={src}
          {...rest}
          style={{ cursor: 'zoom-in', ...rest.style }}
        />
      </PhotoView>
    </PhotoProvider>
  );
};
