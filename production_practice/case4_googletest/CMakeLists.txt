cmake_minimum_required(VERSION 3.20)

project(synergy_container_contracts LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(container_interfaces INTERFACE)
target_include_directories(
    container_interfaces
    INTERFACE
    "${CMAKE_CURRENT_SOURCE_DIR}/include"
)

option(BUILD_CONTRACT_TESTS "Build GoogleTest contracts with a supplied implementation" OFF)
set(
    CONTAINER_IMPLEMENTATION
    ""
    CACHE FILEPATH
    "Source file that defines make_queue, make_max_heap and make_binary_tree"
)

if(BUILD_CONTRACT_TESTS)
    if(NOT CONTAINER_IMPLEMENTATION OR NOT EXISTS "${CONTAINER_IMPLEMENTATION}")
        message(
            FATAL_ERROR
            "Set CONTAINER_IMPLEMENTATION to an existing implementation source file."
        )
    endif()

    enable_testing()
    find_package(GTest REQUIRED)

    add_executable(
        containers_contract_tests
        tests/containers_test.cpp
        "${CONTAINER_IMPLEMENTATION}"
    )
    target_link_libraries(
        containers_contract_tests
        PRIVATE
        container_interfaces
        GTest::gtest_main
    )

    include(GoogleTest)
    gtest_discover_tests(containers_contract_tests)
endif()
