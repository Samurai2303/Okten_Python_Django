import {useEffect, useState} from "react";
import axios from "axios";

function App() {
    let [cars, setCars] = useState([]);

    useEffect(() => {
        axios.get('/api/cars').then((value => {
            setCars(value.data);
        }));
    }, [])


    return (
        <div>
            <h1>Cars</h1>
            {/*{cars.map(value => <div key={value.id}>{value.model}</div>)}*/}

        </div>
    );
}

export default App;
