import React from 'react';
import {Grid, Container, Segment, Menu, Message} from 'semantic-ui-react';

// import Items from "./Items.js"

class CameraCollection extends React.Component{

    state = {
        activeItem: "Overview",
        CardData: {},
        Images: {
            N: "./images/cw66.gif",
            W: "./images/cw72.gif",
            E: "./images/cw68.gif",
            S: "./images/cw70.gif"
        },
        Thumbs:{
            N: "./images/thumbs/cw66.gif",
            W: "./images/thumbs/cw72.gif",
            E: "./images/thumbs/cw68.gif",
            S: "./images/thumbs/cw70.gif"
        }
    }
    props = {
        Datapath: "./data/SensorDump.json"
    }

    constructor(props){
        super(props);
        
        fetch(this.props.Datapath)
        .then(response => response.json())
        .then(json => {
            this.setState({
                CardData: json
                })
        });
    }

    FormattedData(){

        function UniqueRequests(data){
            var UniqueSet = []
            var TrackerSet = []
            data.forEach( (y) => {
                if(TrackerSet.includes(y.Label)){
                }
                else{
                    UniqueSet.push(y);
                    TrackerSet.push(y.Label);
                }
            })
            return UniqueSet;
        };

        const d = Object.values(this.state.CardData);
        const p = Object.values(d);
        const f = d.filter(x => x.RequestString === undefined );
        const c = f.map(x => Object.values(x));
        const v = c.reduce((a,e) => a.concat(e),[]);
        const final = UniqueRequests(v);

        console.log(final);
        
        return final;
    }

    ConstructPil(fullhref, smallhref){
        const Container = {
            overflow: "hidden"
            };
        const Image = {
            width: "100%"
            };
        return(
            <div style={Container}>
                <img src={fullhref} style={Image} />
                {/* <ProgressiveImage
                    preview={smallhref}
                    src={fullhref}
                    transitionTime={1000}
                    transitionFunction="ease-in"
                    render={(src, style) => <img src={src} style={{...style, ...Image}} />}
                /> */}
            </div>
        )
    }

    HumidityTooltip(DirStr, Value){
        if(Value <= 60){
            return(
                <div style={{backgroundColor:"#FFF"}}>
                    {DirStr}<br/>Humidity: {Value} %
                </div>
            )
        }
        else if(Value <= 80){
            return(
                <div style={{backgroundColor:"#F63"}}>
                    {DirStr}<br/>Humidity: {Value} %
                </div>
            )
        }
        else{
            return(
                <div style={{backgroundColor:"#F33"}}>
                    {DirStr}<br/>Humidity: {Value} %
                </div>
            )
        }
    }

    QuadLayout(Data){ 
        // const {a,b,...c} = Data;//Data.find((o) => o.Label === "Inside Humidity");
        // const NW = Data.find((o) => o.Label === "Inside Humidity");
        // const SE = Data.find((o) => o.Label === "Inside Humidity");
        // const SW = Data.find((o) => o.Label === "Inside Humidity");

        // console.log(Data[1]["Value"]);
        // console.log(b);
        // console.log(c);

        return (
            <Segment.Group vertical>
                <Segment.Group horizontal>
                    <Segment textAlign={"center"}>
                        {this.ConstructPil(this.state.Images.N, this.state.Thumbs.N)}
                        North<br/>Humidity: - - -
                    </Segment>
                    <Segment textAlign={"center"}>
                        {this.ConstructPil(this.state.Images.W, this.state.Thumbs.W)}
                        West<br/>Humidity: - - -
                    </Segment>
                </Segment.Group>
                <Segment.Group horizontal>
                    <Segment textAlign={"center"}>
                        {this.ConstructPil(this.state.Images.E, this.state.Thumbs.E)}
                        East<br/>Humidity: - - -
                    </Segment>
                    <Segment textAlign={"center"}>
                        {this.ConstructPil(this.state.Images.S, this.state.Thumbs.S)}
                        South<br/>Humidity: - - -
                    </Segment>
                </Segment.Group>
            </Segment.Group>
            // <Grid columns={2} compact>
            //     <Grid.Row>
            //         <Grid.Column>
            //             {this.ConstructPil(this.state.Images.N, this.state.Thumbs.N)}
            //         </Grid.Column>
            //         <Grid.Column>
            //             {this.ConstructPil(this.state.Images.W, this.state.Thumbs.W)}
            //         </Grid.Column>
            //     </Grid.Row>
            //     <Grid.Row>
            //         <Grid.Column>
            //             {this.ConstructPil(this.state.Images.E, this.state.Thumbs.E)}
            //         </Grid.Column>
            //         <Grid.Column>
            //             {this.ConstructPil(this.state.Images.S, this.state.Thumbs.S)}
            //         </Grid.Column>
            //     </Grid.Row>
            // </Grid>
        );
    }

    VerticalLayout = (
        <Grid columns={1} celled={"internally"}>
            <Grid.Row>
                {this.ConstructPil(this.state.Images.N, this.state.Thumbs.N)}
            </Grid.Row>
            <Grid.Row>
                {this.ConstructPil(this.state.Images.W, this.state.Thumbs.W)}
            </Grid.Row>
            <Grid.Row>
                {this.ConstructPil(this.state.Images.E, this.state.Thumbs.E)}
            </Grid.Row>
            <Grid.Row>
                {this.ConstructPil(this.state.Images.S, this.state.Thumbs.S)}
            </Grid.Row>
        </Grid>
    );
    
    HandleItemClick = (e, { name }) => this.setState({ activeItem: name })

    render(){

        const { activeItem } = this.state
        const menu = {
            width: "100%"
        }

        var values = [];

        return(
            <Container fluid stretched >

                <Menu fluid pointing style={menu} attached={"bottom"}>
                    <Menu.Item 
                        as={"a"}
                        name={"Overview"}
                        active={activeItem === "Overview"} 
                        onClick={this.HandleItemClick} 
                    />
                    <Menu.Item
                        as={"a"}
                        name={"N"}
                        active={activeItem === "N"}
                        onClick={this.HandleItemClick}
                    />
                    <Menu.Item
                        as={"a"}
                        name={"W"}
                        active={activeItem === "W"}
                        onClick={this.HandleItemClick}
                    />
                    <Menu.Item
                        as={"a"}
                        name={"E"}
                        active={activeItem === "E"}
                        onClick={this.HandleItemClick}
                    />
                    <Menu.Item
                        as={"a"}
                        name={"S"}
                        active={activeItem === "S"}
                        onClick={this.HandleItemClick}
                    />
                </Menu>

                {/* <Segment.Group> */}

                    
                    {activeItem==="Overview" && this.QuadLayout(this.FormattedData())}
                    {activeItem==="N" && <Segment> {this.ConstructPil(this.state.Images.N, this.state.Thumbs.N)} </Segment>}
                    {activeItem==="W" && <Segment> {this.ConstructPil(this.state.Images.W, this.state.Thumbs.W)} </Segment>}
                    {activeItem==="E" && <Segment> {this.ConstructPil(this.state.Images.E, this.state.Thumbs.E)} </Segment>}
                    {activeItem==="S" && <Segment> {this.ConstructPil(this.state.Images.S, this.state.Thumbs.S)} </Segment>}
                    

                    {/* <Segment.Group horizontal>
                        <Segment textAlign={"center"} color={"grey"}>
                            North<br/>Humidity: - - -
                        </Segment>
                        <Segment textAlign={"center"} color={"grey"}>
                            West<br/>Humidity: - - -
                        </Segment>
                        <Segment textAlign={"center"} color={"grey"}>
                            East<br/>Humidity: - - -
                        </Segment>
                        <Segment textAlign={"center"} color={"grey"}>
                            South<br/>Humidity: - - -
                        </Segment>
                    </Segment.Group> */}
                    
                {/* </Segment.Group> */}
                
            </Container>
        )
    };

}

export default CameraCollection;