import React from 'react';
import {Image, Container, Menu} from 'semantic-ui-react';

// import Items from "./Items.js"
import Overview from "./Overview.js"

import GraphCollection from "./GraphCollection.js"
import CameraCollection from "./CameraCollection.js"
import DetailCollection from "./DetailCollection.js"

class Index extends React.Component {

    state = {
        MenuState: "Overview"
    }

    HandleItemClick = (e, { name }) => this.setState({ MenuState: name })

    render(){
        
        const NavBar = (
            <Menu stackable attached>

                <Menu.Item as={"a"} header href={"https://www.naoj.org/"}>  
                    <Image size={"mini"} src={"/favicon.ico"} style={{ marginRight: '1.5em' }} />
                    Subaru Weather<br/>Application
                </Menu.Item>

                <Menu.Menu position={"right"}>
                    <Menu.Item as='a' name={"Overview"}        onClick={this.HandleItemClick}>Overview</Menu.Item>
                    <Menu.Item as='a' name={"Graphs"}          onClick={this.HandleItemClick}>Graphs</Menu.Item>
                    <Menu.Item as='a' name={"Data"}            onClick={this.HandleItemClick}>Data</Menu.Item>
                    <Menu.Item as='a' name={"SecurityCameras"} onClick={this.HandleItemClick}>Security cameras</Menu.Item>
                </Menu.Menu>

            </Menu>
        );

        return(
            <div>
                {NavBar}
                {this.state.MenuState === "Overview" && <Overview/>}
                {this.state.MenuState === "Graphs" && <Container stretched style={{paddingTop: "1em"}}><GraphCollection/></Container>}
                {this.state.MenuState === "Data" && <Container stretched style={{paddingTop: "1em"}}><DetailCollection/></Container>}
                {this.state.MenuState === "SecurityCameras" && <Container stretched style={{paddingTop: "1em"}}><CameraCollection/></Container>}
            </div>
        )
    }
}

export default Index;
