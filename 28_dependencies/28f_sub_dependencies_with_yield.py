from typing import Annotated

from fastapi import Depends

# Assuming these are the dependency classes

async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a 
    finally:
        dep_a.close() # This will close dep_a after it is done


async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):   
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a) # This will close dep_a after dep_b is done


async def dependency_c(dep_b: Annotated[DepB, Depends(dependency_b)]):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b) # This will close dep_b after dep_c is done