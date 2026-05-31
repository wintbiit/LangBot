from langbot.pkg.platform.sources.lark import _format_lark_text_message


def test_format_compact_diagnostic_answer():
    raw = (
        '结论：节点资源占用存在异常依据：'
        '1.k3s-server-2CPU占用高达95%，内存占用58%'
        '2.k3s-server-1CPU占用53%，内存占用58%'
        '3.robotlab-misumiCPU占用52%，内存占用50%'
        '4.k3s-server-0资源占用相对正常（CPU5%，内存41%）'
        '建议下一步：'
        '1.检查k3s-server-2上运行的Pod'
        '2.排查k3s-server-1和robotlab-misumi的持续高负载原因'
        '3.关注k3s-server-0是否负载过低需要重新调度'
    )

    formatted = _format_lark_text_message(raw)

    assert '异常\n\n依据：' in formatted
    assert '\n1. k3s-server-2CPU占用高达95%' in formatted
    assert '\n2. k3s-server-1CPU占用53%' in formatted
    assert '\n\n建议下一步：' in formatted
    assert '\n3. 关注k3s-server-0是否负载过低需要重新调度' in formatted


def test_format_preserves_versions_and_decimals():
    raw = '依据：根据RoboMaster 2026通信协议V1.3.1，字段长度为2字节，阈值为0.75。建议：检查0x0A05。'

    formatted = _format_lark_text_message(raw)

    assert 'V1.3.1' in formatted
    assert '0.75' in formatted
    assert '0x0A05' in formatted
    assert '\n\n建议：' in formatted
