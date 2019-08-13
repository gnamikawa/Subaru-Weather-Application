import React from 'react';
import {Card, Image, Container} from 'semantic-ui-react';

// import Items from "./Items.js"

class GraphCollection extends React.Component{

    props = {
        datapath: "./data/graphs.json",
    }

    state = {
        cardData: {}, //Json object to represent cards
    }

    constructor(props){

        super(props);

        //Fetch JSON information about the cards
        fetch(this.props.datapath)
        .then(response => response.json())
        .then(json => {
            this.setState({
                cardData: json
            });
        });

    }
    
    render(){

        const cardlist = Object.values(this.state.cardData).map((elem) => ({
            src: elem.src,
            alt: elem.alt,
            href: elem.href,
            header: elem.header,
            description: elem.description,
            cardrender: 
                <Card fluid link compact href={elem.href}>
                    <Image
                        style={{objectFit: "contain"}} 
                        // style={{height: 300, objectFit: "fit"}} 
                        src={elem.href}
                    />

                    <Card.Content>
                        <Card.Header> {elem.header} </Card.Header>
                        {/* <Card.Meta> Updated last at {elem.} </Card.Meta> */}
                        <Card.Description> {elem.description} </Card.Description>
                    </Card.Content>

                </Card>
        }));

        return ( 
            <Container>
                {cardlist.map(x => x.cardrender)}
            </Container>
        );
    };

}

export default GraphCollection;