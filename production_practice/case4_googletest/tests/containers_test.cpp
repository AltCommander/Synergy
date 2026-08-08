#include "containers.hpp"

#include <gtest/gtest.h>

#include <stdexcept>

TEST(QueueContract, StartsEmptyAndUsesFifoOrder) {
    auto queue = make_queue();

    ASSERT_NE(queue, nullptr);
    EXPECT_TRUE(queue->empty());

    queue->push(10);
    queue->push(20);
    queue->push(30);

    EXPECT_FALSE(queue->empty());
    EXPECT_EQ(queue->pop(), 10);
    EXPECT_EQ(queue->pop(), 20);
    EXPECT_EQ(queue->pop(), 30);
    EXPECT_TRUE(queue->empty());
}

TEST(QueueContract, PopFromEmptyQueueThrows) {
    auto queue = make_queue();

    ASSERT_NE(queue, nullptr);
    EXPECT_THROW(queue->pop(), std::underflow_error);
}

TEST(MaxHeapContract, PopsValuesFromLargestToSmallest) {
    auto heap = make_max_heap();

    ASSERT_NE(heap, nullptr);
    heap->push(4);
    heap->push(12);
    heap->push(7);
    heap->push(12);

    EXPECT_EQ(heap->pop(), 12);
    EXPECT_EQ(heap->pop(), 12);
    EXPECT_EQ(heap->pop(), 7);
    EXPECT_EQ(heap->pop(), 4);
    EXPECT_TRUE(heap->empty());
}

TEST(MaxHeapContract, PopFromEmptyHeapThrows) {
    auto heap = make_max_heap();

    ASSERT_NE(heap, nullptr);
    EXPECT_THROW(heap->pop(), std::underflow_error);
}

TEST(BinaryTreeContract, PushSearchAndPopWorkTogether) {
    auto tree = make_binary_tree();

    ASSERT_NE(tree, nullptr);
    EXPECT_FALSE(tree->search(8));
    EXPECT_FALSE(tree->pop(8));

    for (int value : {8, 3, 10, 1, 6, 14}) {
        tree->push(value);
    }

    EXPECT_TRUE(tree->search(1));
    EXPECT_TRUE(tree->search(10));
    EXPECT_TRUE(tree->pop(3));
    EXPECT_FALSE(tree->search(3));
    EXPECT_FALSE(tree->pop(99));
}
