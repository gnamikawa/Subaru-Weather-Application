import React from 'react';

import {Grid} from 'semantic-ui-react';
// import Items from "./Items.js"
import CameraCollection from "./CameraCollection.js"
import GraphCollection from "./GraphCollection.js"
import DetailCollection from "./DetailCollection.js"
// import InteractiveLineplot from "./InteractiveLineplot.js"

class Overview extends React.Component {
    render(){
        return (
            // <InteractiveLineplot id={"interactivePlot"} width={800} height={500}/>
            <Grid columns={2} divided stackable stretched padded style={{height: "100%"}} verticalAlign={"top"}>

               <Grid.Column stretched width={7}>
                   <CameraCollection/>
                   <DetailCollection/>
               </Grid.Column>

               <Grid.Column stretched width={9}>
                   <GraphCollection/>
               </Grid.Column>

            </Grid>
        )
    }
}

export default Overview;
