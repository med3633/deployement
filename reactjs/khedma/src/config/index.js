//export const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
import { useMemo } from "react";
import { useLocation } from "react-router";

// export const API_URL="https://51.255.49.204:8000";
export const API_URL="http://backend:8000";


export const useQuery=()=>{
    const { search } = useLocation();

    return useMemo(() => new URLSearchParams(search), [search]);
}