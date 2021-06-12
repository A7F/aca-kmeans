cmake_minimum_required(VERSION 3.13)
project(aca_kmeans)

set(CMAKE_CXX_STANDARD 14)

# these following directives disable dynamic threads and force use of defined following number of threads
# corresponds to omp_set_dynamic(0) from code
set(ENV{OMP_DYNAMIC} 0)

find_package(OpenMP REQUIRED)

add_executable(aca_kmeans serial.cpp)

if(OpenMP_CXX_FOUND)
    target_link_libraries(aca_kmeans PUBLIC OpenMP::OpenMP_CXX)
endif()
