// src/api.js
import axios from 'axios';

const BASE_URL = 'http://20.244.56.144/test';

export const fetchProducts = async (companyName, categoryName, topN, minPrice, maxPrice) => {
  const response = await axios.get(`${BASE_URL}/companies/${companyName}/categories/${categoryName}/products/top-${topN}&minPrice=${minPrice}&maxPrice=${maxPrice}`);
  return response.data;
};