import React, { useState } from "react";
import * as XLSX from "xlsx";
import "./XcelFileToTable.css";


const XcelFileToTable = () => {

    const [data, setData] = useState([]);

    const handleFIleUpload = (e)=>{

        let file = e.target.files[0];


        const reader = new FileReader();

        reader.readAsBinaryString(file);

        reader.onload = (ev)=>{
            let bString = ev.target.result;
            console.log("bString:- ", bString)

            let workBench = XLSX.read(bString, {type:"binary"});
            console.log("workBench :-", workBench);

            let SheetName = workBench.SheetNames[0];
            console.log("SheetName :-", SheetName);

            let Sheet = workBench.Sheets[SheetName];
            console.log("Sheet :-", Sheet);

            let JsonData = XLSX.utils.sheet_to_json(Sheet);

            console.log(JsonData);
            setData(JsonData);
        }
    }



    return (

        <div>
              <h1>Xcel Importer</h1>

              <input
                 type="file"
                 accept=".xlsx, .xls, .csv"
                 onChange={handleFIleUpload}
              
              />

              <table>
                  <thead>
                    <tr>
                      {
                        data[0] && Object.keys(data[0]).map((key, i)=>(
                             <th key={key}>{key}</th>
                        ))
                      }
                    </tr>
                  </thead>

                  <tbody>
                      {
                        data.map((row, i)=>(
                            <tr key={i}>
                                {
                                    Object.values(row).map((value, i)=>(
                                        <td key={i}>{value}</td>
                                    ))
                                }
                            </tr>
                        ))
                      }
                  </tbody>
              </table>
        </div>
    )
}


export default XcelFileToTable;