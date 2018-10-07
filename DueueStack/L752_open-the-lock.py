from collections import deque


class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        length = len(target)
        # bfs，可以想象成多叉树
        # 比如target = 7,deadends= [5]
        # 那么new_taget_list = [8,6]
        # compare_queue = deque([7],[8,6],[7,9,5,7])，由于7已经比较过了，所以不再入队列，因此需要一个集合来去重
        # 即compare_queue = deque([7],[8,6],[9,5]),这里面3个列表表示cnt=3,当list中有0的时候表示取到需要的值了，如果new_target_list ==[]， 表示deadends已经阻完全了，不可能取到target
        compare_queue = deque()
        searched_target = set()
        compare_queue.append([target])
        deadends_set = set(deadends)
        count = 0
        while compare_queue:
            cur_target_list = compare_queue.popleft()
            new_target_list = []
            while cur_target_list != []:
                cur_target = cur_target_list.pop()
                if cur_target == '0000':
                    return count
                for idx in range(length):
                    i = str(int(int(cur_target[idx]) + 1))[-1]
                    j = str(int(int(cur_target[idx]) - 1))[-1]
                    new_target_i = cur_target[0:idx] + i + cur_target[idx + 1:]
                    new_target_j = cur_target[0:idx] + j + cur_target[idx + 1:]
                    if new_target_i not in searched_target and new_target_i not in deadends_set:
                        searched_target.add(new_target_i)
                        new_target_list.append(new_target_i)
                    if new_target_j not in searched_target and new_target_j not in deadends_set:
                        searched_target.add(new_target_j)
                        new_target_list.append(new_target_j)
            if new_target_list == []:
                return -1
            compare_queue.append(new_target_list)
            count += 1


if __name__ == '__main__':
    s = Solution()
    l1 = s.openLock(deadends=["8687","6666","7686","8876","7676","6777","6876","8776","8768","8776","6776","7677","6676","7786","7768","7678","7888","6887","8788","8887","8866","8886","7876","8767","8787","6767","8788","6776","6786","8677","8687","7868","8668","7676","7668","7768","7787","8876","7876","7677","8687","7768","7768","6776","6887","6766","8687","6678","6668","7687","6686","8676","7787","7877","8766","7787","7867","6778","7767","8876","6688","8778","6776","6776","8768","8867","7876","8678","6666","6678","6787","6676","6777","7676","7786","6778","6776","6888","7866","8677","8876","8886","8776","6777","8787","7787","6678","7677","8678","8686","8866","7877","7678","6886","7876","7687","6666","7786","7767","7686","6887","6678","7886","7678","6878","6678","7868","6677","7877","8768","7688","7766","6688","8786","7877","8767","6878","7767","7678","8676","6677","8887","8687","8778","6666","6866","7788","7766","6778","8668","8677","7666","6687","6668","6788","6878","8668","7676","6768","7887","8676","8876","6767","6887","6886","7866","7886","6687","6687","8778","6787","6767","8688","7686","7678","6686","8876","7777","7786","8668","7666","7788","7876","8766","7777","6876","7868","8878","6677","7666","7777","8867","8767","6768","7767","7866","6766","8878","6777","8886","7886","7776","7786","8668","7768","7867","6686","6786","6777","7768","6678","8867","6866","8888","7667","7887","8786","8887","6877","6677","6886","8877","8677","6667","8766","6677","7668","8888","6776","6668","6866","7667","7886","7886","7788","6678","7767","8686","6776","7676","6866","6886","6786","6686","7676","8886","7666","7776","8877","6666","6867","8887","6687","7776","6888","8888","7776","8767","8767","6868","7766","7867","7777","7667","6867","7888","6777","6686","6666","7786","7878","7686","7666","8876","8686","7688","8766","8887","6776","8686","8686","7788","8887","7778","7886","7676","7668","8666","8677","7866","6676","6888","6868","7687","7687","6887","7786","6677","6788","8777","8686","6776","6887","6867","8778","6867","8768","7687","8787","8778","6668","6787","6766","6678","6667","7667","8788","7686","7887","6868","7676","8668","6786","7778","8778","8867","7787","7786","7667","8867","7888","8678","6678","6778","6767","8666","8666","7867","8677","8676","6867","7877","7888","6677","7888","8666","8788","7866","8668","7787","7787","6776","8767","6886","6777","6887","8788","7877","7766","6787","8688","7867","8777","6668","8767","6686","7888","7867","7776","6668","8687","8666","7768","8768","6678","8786","6668","6777","8788","6686","8686","8867","6676","7787","7866","6767","6786","8868","8886","6678","7868","7767","8668","8787","7778","7687","6877","8688","6787","7887","6788","6688","8768","8678","8887","6887","6888","7678","8886","6766","7676","7786","6788","8777","7666","6687","6687","6887","7867","8677","6787","7786","8788","8886","6686","7887","6678","8676","7887","8688","7667","8768","7788","6687","7876","7686","8776","7688","8868","8777","6668","8768","7686","7776","6868","8886","8866","6777","7876","7668","8676","8668","8676","6878","7867","6878","6676","8688","8866","7666","8776","7666","6876","7867","8876","8666","8666","7687","6766","6687","7776","8766","6777","6687","7767","8676","7768","8786","7788","6788","8786","6686","6676","8876","7787","6787","8886","6687","7886","8687","6878","6667","6787","8676","6676","6888","6677","8876","8778","6676","7677","8677","6667","7687","7667","7878","7788","7767","8867","7768","7878","7677","8878","7776","6686","8666","8688","8868","7776","9667"], target="8667")
    print(l1)
