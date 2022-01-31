import React from 'react';
import ImagesView from './ImagesView';

interface IImagesContainerProps {
}

export interface IImagesViewProps {
}

const ImagesContainer=(props: IImagesContainerProps) => {
   const { } = props

   const passProps: IImagesViewProps = {

   }

   return <ImagesView {...passProps}/>
} 

ImagesContainer.defaultProps = {

} 

export default ImagesContainer;
