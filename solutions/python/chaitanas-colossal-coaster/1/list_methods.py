"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(
    express_queue: list[str],
    normal_queue: list[str],
    ticket_type: int,
    person_name: str,
) -> list[str]:
    """Add a person to the express or normal queue based on the ticket number.

    :param express_queue: The names in the fast-track queue.
    :param normal_queue: The names in the normal queue.
    :param ticket_type: Type of ticket. 1 = express, 0 = normal.
    :param person_name: The name of the person to add to a queue.
    :return: The updated queue the name was added to.
    """
    if ticket_type:
        express_queue.append(person_name)
    else:
        normal_queue.append(person_name)
    return express_queue if ticket_type else normal_queue


def find_my_friend(queue: list[str], friend_name: str) -> int:
    """Search the queue for a name and return their queue position (index).

    :param queue: The names in the queue.
    :param friend_name: The name of the friend to find.
    :return: The index at which the friend's name was found.
    """
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: The names in the queue.
    :param index: The index at which to add the new name.
    :param person_name: The name to add.
    :return: The queue updated with the new name.
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    """Remove the mean person from the queue by the provided name.

    :param queue: The names in the queue.
    :param person_name: The name of the mean person.
    :return: The queue updated with the mean person's name removed.
    """
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list[str], person_name: str) -> int:
    """Count how many times the provided name appears in the queue.

    :param queue: The names in the queue.
    :param person_name: The name you wish to count or track.
    :return: The number of times the name appears in the queue.
    """
    return queue.count(person_name)


def remove_the_last_person(queue: list[str]) -> str:
    """Remove the person at the last index from the queue and return their name.

    :param queue: The names in the queue.
    :return: The name that has been removed from the end of the queue.
    """
    return queue.pop()


def sorted_names(queue: list[str]) -> list[str]:
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: The names in the queue.
    :return: A copy of the queue in alphabetical order.
    """
    return sorted(queue)
