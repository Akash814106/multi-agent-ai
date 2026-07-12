import { useState } from "react";
import axios from "axios";

export default function useAuth() {

    const [user, setUser] = useState(

        localStorage.getItem("username") || ""

    );

    const [token, setToken] = useState(

        localStorage.getItem("token") || ""

    );

    async function register(

        username,
        email,
        password

    ) {

        await axios.post(

            "http://127.0.0.1:8000/register",

            {
                username,
                email,
                password,
            }

        );

    }

    async function login(

        email,
        password

    ) {

        const response = await axios.post(

            "http://127.0.0.1:8000/login",

            {
                email,
                password,
            }

        );

        localStorage.setItem(

            "token",

            response.data.access_token

        );

        localStorage.setItem(

            "username",

            response.data.username

        );

        setToken(

            response.data.access_token

        );

        setUser(

            response.data.username

        );

    }

    function logout() {

        localStorage.removeItem("token");

        localStorage.removeItem("username");

        setToken("");

        setUser("");

    }

    return {

        user,

        token,

        login,

        register,

        logout,

    };

}