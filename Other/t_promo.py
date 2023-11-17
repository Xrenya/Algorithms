import heapq
import pytest

# Gives prices, k number of promo coupons, x discount price
# New price can be found prices[i] = max(prices[i] - x, 0)
# Find the smallest amount can be paid using promo


def max_save(prices, k, x):
    prices = [-x for x in prices]
    heapq.heapify(prices)
    print(prices)
    while k:
        max_price = -heapq.heappop(prices)
        diff = max(max_price - x, 0)
        heapq.heappush(prices, -diff)
        k -= 1
    return sum([-x for x in prices])



@pytest.mark.parametrize(
    "input,output", [
        ([[8,3,10,5,13], 4, 7], 12)
    ]
)
def test_max_save(input, output):
    total_paid = max_save(*input)
    assert total_paid == output, (f"Expected value '{output}', but got '{total_paid}'")
