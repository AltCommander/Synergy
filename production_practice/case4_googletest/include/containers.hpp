#pragma once

#include <memory>

template <class T>
class IQueue {
public:
    virtual ~IQueue() = default;

    virtual void push(const T& value) = 0;
    virtual T pop() = 0;
    [[nodiscard]] virtual bool empty() const noexcept = 0;
};

template <class T>
class IMaxHeap {
public:
    virtual ~IMaxHeap() = default;

    virtual void push(const T& value) = 0;
    virtual T pop() = 0;
    [[nodiscard]] virtual bool empty() const noexcept = 0;
};

class IBinaryTree {
public:
    virtual ~IBinaryTree() = default;

    virtual void push(int value) = 0;
    virtual bool pop(int value) = 0;
    [[nodiscard]] virtual bool search(int value) const noexcept = 0;
};

std::unique_ptr<IQueue<int>> make_queue();
std::unique_ptr<IMaxHeap<int>> make_max_heap();
std::unique_ptr<IBinaryTree> make_binary_tree();
