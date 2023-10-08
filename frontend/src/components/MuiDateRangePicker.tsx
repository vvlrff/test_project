import { useState, useEffect } from 'react';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { Button } from '@mui/material';
import { usePostAllNewsMutation } from '../services/newsApi';

const MuiDateRangePicker = ({}) => {
    const [firstValue, setFirstValue] = useState<any>([]);
    const [secondValue, setSecondValue] = useState<any>([]);
    const [searchRequest, setSearchRequest] = useState('');
    
    const sendData = () => {
        console.log(firstValue)
        console.log(secondValue)
        console.log(searchRequest)
    }

    return (
        <>
            <input
                placeholder="Поиск новостей"
                value={searchRequest}
                onChange={(e) => setSearchRequest(e.target.value)}
                type="text"
            />
            <LocalizationProvider dateAdapter={AdapterDayjs}>
                <DatePicker
                    label="От"
                    value={firstValue}
                    onChange={(newValue) => setFirstValue(newValue)}
                />
                <DatePicker
                    label="До"
                    value={secondValue}
                    onChange={(newValue) => setSecondValue(newValue)}
                />
                <Button
                    variant="contained"
                    color="primary"
                    onClick={sendData}
                >
                    Искать
                </Button>
            </LocalizationProvider>
        </>
    );
}

export default MuiDateRangePicker

