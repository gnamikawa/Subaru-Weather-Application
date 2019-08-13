import React from 'react';
import {Table, Container} from 'semantic-ui-react';

// import Items from "./Items.js"

class DetailCollection extends React.Component{

    state = {
        CardData: {}
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

    DataRows(){

        function CreateData(name, idt, data) {
            return { name, idt, data };
        }

        function CategorizeData(dataentries){

            function CreateEpochEntry(container, data){
                const NewDate = new Date(0);
                NewDate.setUTCSeconds(data.Value);
                //container.push(CreateData("Epoch", data.RequestString, data.Value));
                container.push(CreateData("Last Updated", data.RequestString + " (Converted)", new String(NewDate)));
            }
            
            function CreateDataEntry(container, data){
                container.push(CreateData(data.Label, data.RequestString, data.Value))
            }

            const duperows = [];

            for(const [fkey, fvalue] of Object.entries(dataentries)){
                if(fkey === "Epoch"){
                    CreateEpochEntry(duperows, fvalue);
                    continue;
                }
                else{
                    for(const [pkey, pvalue] of Object.entries(fvalue)){
                        CreateDataEntry(duperows, pvalue);
                    }
                    continue;
                }
            }

            return duperows;
        }

        function UniqueRequests(data){
            var UniqueSet = []
            var TrackerSet = []
            data.forEach( (y) => {
                if(TrackerSet.includes(y.idt)){
                }
                else{
                    UniqueSet.push(y);
                    TrackerSet.push(y.idt);
                }
            })
            return UniqueSet;
        };

        return UniqueRequests(CategorizeData(this.state.CardData));

    }
    
    render(){

        const Rows = this.DataRows();

        const Tableheaders = (
            <Table.Row>
                <Table.HeaderCell>Name</Table.HeaderCell>
                <Table.HeaderCell>Identifier</Table.HeaderCell>
                <Table.HeaderCell>Data</Table.HeaderCell>
            </Table.Row>
        );

        const Tablerows = Rows.map(row => (
            <Table.Row>
                <Table.Cell> {row.name} </Table.Cell>
                <Table.Cell> {row.idt} </Table.Cell>
                <Table.Cell> {row.data} </Table.Cell>
            </Table.Row>
        ));

        return ( 
            <Container fluid stretched style={{marginTop: "1em"}}>
                <Table structured fixed compact selectable stackable>
                    <Table.Header> {Tableheaders} </Table.Header>
                    <Table.Body> {Tablerows} </Table.Body>
                </Table>
            </Container>
        );
    };

}

export default DetailCollection;
