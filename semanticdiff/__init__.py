from __future__ import absolute_import

import sys

if sys.version_info[0] == 3:
    from . import _diff_match_patch_py3 as diff_match_patch
else:
    from . import _diff_match_patch_py2 as diff_match_patch


def format_diff(diff, left, right):
    result = []
    for opcode in diff:
        if isinstance(opcode, tuple):
            if len(opcode) == 5:
                # difflib
                op, sl, el, sr, er = opcode
                if op == 'equal':
                    result.append('= %s' % left[sl:el])
                elif op == 'replace':
                    result.append('/ %s/%s' % (left[sl:el], right[sr:er]))
                elif op == 'insert':
                    result.append('+ %s' % right[sr:er])
                elif op == 'delete':
                    result.append('- %s' % left[sl:el])
            elif len(opcode) == 2:
                diff_match_patch
                op, text = opcode
                if op == -1:
                    result.append('- %s' % text)
                elif op == 0:
                    result.append('= %s' % text)
                elif op == 1:
                    result.append('+ %s' % text)


    return '\n'.join(result)


def diff_text(left, right):
    dmp = diff_match_patch.diff_match_patch()
    diffs = dmp.diff_main(left, right)
    dmp.diff_cleanupSemantic(diffs)
    return diffs
