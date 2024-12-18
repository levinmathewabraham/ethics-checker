const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();

const app = express();

// Test Route
app.get('/', (req, res) => {
    res.send('Server is running and connected to MongoDB');
});

// MongoDB Connection
mongoose
    .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB Connected'))
    .catch((err) => console.error(err));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
