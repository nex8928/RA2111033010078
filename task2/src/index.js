// src/components/ProductList.js
import React, { useState, useEffect } from 'react';
import { fetchProducts } from '../api';

const ProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const getProducts = async () => {
      const data = await fetchProducts('AMZ', 'Laptop', 10, 1, 10000);
      setProducts(data);
    };
    getProducts();
  }, []);

  return (
    <div>
      {products.map((product, index) => (
        <div key={index}>
          <h2>{product.productName}</h2>
          {/* Display other product details */}
        </div>
      ))}
    </div>
  );
};

export default ProductList;