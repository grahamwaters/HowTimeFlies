import React from 'react';
import Wiki_imagesView from './Wiki_imagesView';

interface IWiki_imagesContainerProps {
}

export interface IWiki_imagesViewProps {
}

const Wiki_imagesContainer=(props: IWiki_imagesContainerProps) => {
   const { } = props

   const passProps: IWiki_imagesViewProps = {

   }

   return <Wiki_imagesView {...passProps}/>
} 

Wiki_imagesContainer.defaultProps = {

} 

export default Wiki_imagesContainer;
