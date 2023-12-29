import React from "react";
import { createRoot } from 'react-dom/client';
import Root from "./client/Root";

const root = createRoot(document.getElementById('root'));
root.render(<Root />);