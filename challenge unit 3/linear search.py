def linearsearchproduct(productlist, targetproduct):
    indices = []
    
    for index, product in enumerate(productlist):
        if product == targetproduct:
          indices.append(index)
            
    return indices


#Example usage:
products = ["shoes", "boot", "loafter", "shoes", "sandal", "shoes"]
target= "shoes"
target2 = 'apple'
result = linearsearchproduct(products,target)
print(result)
             
    
                        
